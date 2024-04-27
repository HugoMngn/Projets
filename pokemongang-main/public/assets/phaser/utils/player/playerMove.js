import { client, updateAnimationPlayer } from "../index.js";

function playerMove(time) {
  if (time - this.lastUpdateTime >= this.updateInterval) {
    const keys = client.keys.keys;
    const upKey = keys.up.isDown;
    const downKey = keys.down.isDown;
    const rightKey = keys.right.isDown;
    const leftKey = keys.left.isDown;
    const prefixRun = keys.shift.isDown ? 'run_' : '';
  
    const map = client.map;

    let x = client.x;
    let y = client.y;

    if(upKey || downKey || rightKey || leftKey) {
      if(downKey) {
        y -= 1;

        client.player.rotation = client.animation.player.rotation.down;
        this.updateAnimationPlayer(`${prefixRun}down`);
      } else if(upKey) {
        y += 1;

        client.player.rotation = client.animation.player.rotation.up;
        this.updateAnimationPlayer(`${prefixRun}up`);
      } else if(rightKey) {
        x -= 1;

        client.player.rotation = client.animation.player.rotation.right;
        this.updateAnimationPlayer(`${prefixRun}right`);
      } else if(leftKey) {
        x += 1;

        client.player.rotation = client.animation.player.rotation.left;
        this.updateAnimationPlayer(`${prefixRun}left`);
      };
      const nextMapXPosition = x * map.sizePixelTile;
      const nextMapYPosition = y * map.sizePixelTile;
      const nextLocalCaseXPlayer = (x - 6) * -1;
      const nextLocalCaseYPlayer = (y - 6) * -1;
      const level =  map.currentLevel.level

      const nextMapXPixel = nextMapXPosition * -1;
      const nextMapYPixel = nextMapYPosition * -1;
      const isMap = (level.leftX < nextMapXPixel && level.rightX > nextMapXPixel) && (level.topX < nextMapYPixel && level.bottomX > nextMapYPixel)
      let teleport = false;

      if(isMap) {
        //const currenTiles = currentMap.collisionLayer.layer.data[localCaseYPlayer][localCaseXPlayer].index - 1;
        const nextCurrentTiles = map.currentLevel.collisionLayer.layer.data[nextLocalCaseYPlayer - 1][nextLocalCaseXPlayer - 1].index - 1;
        const collision = client.map.tiles.find(i => i.id === nextCurrentTiles && i.properties[0].name === client.map.tilesProperties.collision);
        const door = map.currentLevel.level.door.find(i => i.case.find(z => z[0] === client.player.rotation && z[1] === x && z[2] === y));
        if(door) {
          teleport = true;
          client.player.rotation = door.target[0];
          client.x = door.target[1];
          client.y = door.target[2];
          this.multiplayerEmit('saveLastPosition');
        } else if(!collision || !client.settings.collision) {
          client.x = x;
          client.y = y;
        }
      } else if(!client.settings.collision) {
        client.x = x;
        client.y = y;
      };
     
      this.updateLabel(isMap ? map.currentLevel.level.name : 'none')
      this.mapMove(teleport);
      this.updateOtherPlayer(teleport);

      this.multiplayerEmit('playerMove');

      this.lastUpdateTime = time;
    } else if(!upKey && !downKey && !rightKey && !leftKey) {
      updateAnimationPlayer(client.animation.player.idles[client.player.rotation])
    };
  };
};

function convertCoordMapToPlayer(x, y) {
  return {
    x: (x - 6) * -1,
    y: (y - 6) * -1
  };
};

function convertCoordPlayerToMap(x, y) {
  return {
    x: (x - 6) * -1,
    y: (y - 6) * -1,
  }
  };

function updateOtherPlayer(teleport=false) {
  const otherPlayers = client.multiplayer.otherPlayers;
  const xPlayer = (client.x - client.player.data.poseCaseX) * -1 * client.map.sizePixelTile;
  const yPlayer = (client.y - client.player.data.poseCaseY) * -1 * client.map.sizePixelTile;
  const gameWidth = this.game.config.width / 2;
  const gameHeight = this.game.config.height / 2;

  const keys = Object.keys(otherPlayers);
  keys.forEach(key => {
    const x = otherPlayers[key].x * client.map.sizePixelTile - xPlayer + gameWidth;
    const y = otherPlayers[key].y * client.map.sizePixelTile - yPlayer + gameHeight;
    if(!teleport) {
      this.tweens.add({
        targets: otherPlayers[key].player,
        x,
        y,
        duration: this.updateInterval,//window.pokemon.settings.speed.walk,
        ease: 'Linear'
      });
      this.tweens.add({
        targets: otherPlayers[key].username,
        x,
        y: y - client.multiplayer.config.usernameY,
        duration: this.updateInterval,//window.pokemon.settings.speed.walk,
        ease: 'Linear'
      });
    } else {
      otherPlayers[key].player.x = x;
      otherPlayers[key].player.y = y;
      otherPlayers[key].username.x = x;
      otherPlayers[key].username.y = y - client.multiplayer.config.usernameY;
    }
  });
};  

export { playerMove, convertCoordMapToPlayer, convertCoordPlayerToMap, updateOtherPlayer };