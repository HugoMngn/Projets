import { client } from "../index.js";

function multiplayerWorld() {
  //console.log('multiplayerWorld')
  const otherPlayers = client.multiplayer.otherPlayers;
  const socket = client.multiplayer.socket;
  const sizePixelTile = client.map.sizePixelTile;

  socket.on('deleteSelf', () => {
    console.log('deleteSelf', socket.id)
    //console.log(this.scene.destroy)
    //this.scene.stop(client.scenes.name.world)
    this.scene.start(client.scenes.name.stop)
  })
  
  socket.emit('initPlayer', {});

  this.multiplayerEmit('playerMove')

  socket.on('initPlayerRequest', () => this.multiplayerEmit('playerMove'));

  socket.on('playerMoved', (data) => {
    
    const otherPlayer = otherPlayers[data.id];
    //console.log(otherPlayer && (data.scene != this.scene.key || data.world != client.currentIndexWorld))
    //console.log(data.scene != this.scene.key, data.world != client.currentIndexWorld)
    if(otherPlayer && (data.scene != this.scene.key || data.world != client.currentIndexWorld)) {
      //console.log('dont show')
      otherPlayer.player.destroy();
      otherPlayer.username.destroy();
      delete otherPlayers[data.id];
    };
    const xPlayer = (client.x - client.player.data.poseCaseX) * -1 * sizePixelTile;
    const yPlayer = (client.y - client.player.data.poseCaseY) * -1 * sizePixelTile;
    const gameWidth = this.game.config.width / 2;
    const gameHeight = this.game.config.height / 2;

    if(otherPlayer) {
      if(!otherPlayer.player.active) {
        //console.log('delete exite player')
        otherPlayer.player.destroy();
        otherPlayer.username.destroy();
        delete otherPlayers[data.id];
        if(data.scene === this.scene.key && data.world === client.currentIndexWorld) this.createOtherPlayer(otherPlayers, sizePixelTile, xPlayer, yPlayer, gameWidth, gameHeight, data)
      } else {
        //console.log('existe player')
        otherPlayer.lastX = otherPlayer.x;
        otherPlayer.lastY = otherPlayer.y;
        otherPlayer.x = data.x;
        otherPlayer.y = data.y;
        otherPlayer.gender = data.gender; //desact conso trop
        otherPlayer.scene = data.scene;
        otherPlayer.world = data.world;

        otherPlayer.rotation = data.rotation;

        if(data.teleport) {
          otherPlayer.player.x = otherPlayer.x * sizePixelTile - xPlayer + gameWidth;
          otherPlayer.player.y = otherPlayer.y * sizePixelTile - yPlayer + gameHeight;
          otherPlayer.username.x = otherPlayer.x * sizePixelTile - xPlayer + gameWidth;
          otherPlayer.username.y = otherPlayer.y * sizePixelTile - yPlayer + gameHeight - client.multiplayer.config.usernameY;
          data.animation = client.animation.player.idles[data.rotation]
        } else {
          this.tweens.add({
            targets: otherPlayer.player,
            x: otherPlayer.x * sizePixelTile - xPlayer + gameWidth,
            y: otherPlayer.y * sizePixelTile - yPlayer + gameHeight,
            duration: this.updateInterval,
            ease: 'Linear'
          });
          this.tweens.add({
            targets: otherPlayer.username,
            x: otherPlayer.x * sizePixelTile - xPlayer + gameWidth,
            y: otherPlayer.y * sizePixelTile - yPlayer + gameHeight - client.multiplayer.config.usernameY,
            duration: this.updateInterval,
            ease: 'Linear'
          });
        };
        if(!data.animation.startsWith('player_')) data.animation = 'player_' + otherPlayer.gender + '_' + data.animation
        if(otherPlayer.animations.last != data.animation) {
          otherPlayer.animations.last = data.animation;
          otherPlayer.player.play(data.animation);
        };
      };
    } else if(data.scene === this.scene.key && data.world === client.currentIndexWorld){
      //console.log('init new player')
      this.createOtherPlayer(otherPlayers, sizePixelTile, xPlayer, yPlayer, gameWidth, gameHeight, data)
    };
  });

  socket.on('playerDisconnected', (data) => {
    if(otherPlayers[data.id]) {
      otherPlayers[data.id].player.destroy();
      otherPlayers[data.id].username.destroy();
      delete otherPlayers[data.id];
    };
  });

  setInterval(() => {
    const keys = Object.keys(otherPlayers);
    keys.forEach(key => {
      if(otherPlayers[key].x === otherPlayers[key].lastX || otherPlayers[key].y === otherPlayers[key].lastY) {
        const animationName = 'player_' + otherPlayers[key].gender +'_' +client.animation.player.idles[otherPlayers[key].rotation];
        if(otherPlayers[key].animations.last != animationName) {
          otherPlayers[key].animations.last = animationName
          otherPlayers[key].player.play(animationName);
        };
      };
    });
  }, 200);
};

function multiplayerEmit(name) {
  switch(name) {
    case 'playerMove': 
    client.multiplayer.socket.emit('playerMove', {
      ...this.convertCoordMapToPlayer(client.x, client.y),
      rotation: client.player.rotation,
      teleport:false,
      animation: client.animation.player.last,
      gender:client.player.gender,
      world: client.currentIndexWorld,
      scene:this.scene.key
    });
    break;
    case'saveLastPosition':
    client.multiplayer.socket.emit('saveLastPosition', {
      ...this.convertCoordMapToPlayer(client.x, client.y),
      rotation:client.player.rotation,
      world: client.currentIndexWorld,
      gender:client.player.gender,
      scene:this.scene.key
    });
    break;
  }
}

function createOtherPlayer(otherPlayers, sizePixelTile, xPlayer, yPlayer, gameWidth, gameHeight, data) {
  otherPlayers[data.id] = {
    player: this.add.sprite(
      data.x * sizePixelTile - xPlayer + gameWidth, 
      data.y * sizePixelTile - yPlayer + gameHeight, 
      'player')
      .setScale(client.player.data.scale)
      .setOrigin(0.5, 0.5),
    x: data.x,
    y: data.y,
    lastX: data.x,
    lastY: data.y,
    rotation:data.rotation,
    gender:data.gender,
    scene: data.scene,
    world: data.world,
    animations: {
      last: data.animation
    },
    username: this.add.text(
      data.x * sizePixelTile - xPlayer + gameWidth,
      data.y * sizePixelTile - yPlayer + gameHeight - client.multiplayer.config.usernameY, 
      data.username, 
      {
      fontFamily: 'W95FA',
      fontSize:11,
      color: '#ffffff',
      stroke: '#ff0000',
      strokeThickness: 5
    }).setOrigin(0.5)
  };
  client.multiplayer.otherPlayers[data.id].player.play(data.animation);
  this.layer.player.add(otherPlayers[data.id].player);
  this.layer.player.sendToBack(otherPlayers[data.id].player)
  this.layer.text.add(otherPlayers[data.id].username);
}

export { multiplayerWorld, multiplayerEmit, createOtherPlayer };
