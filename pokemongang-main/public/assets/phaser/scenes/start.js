import { client, levels, createAnimationPlayer, convertCoordMapToPlayer, convertCoordPlayerToMap, updateLabel, multiplayerEmit } from "../utils/index.js";

class StartScene extends Phaser.Scene {
  constructor() {
    super({key: client.scenes.name.start});
    this.createAnimationPlayer = createAnimationPlayer.bind(this);
    this.convertCoordMapToPlayer = convertCoordMapToPlayer.bind(this);
    this.convertCoordPlayerToMap = convertCoordPlayerToMap.bind(this);
    this.multiplayerEmit = multiplayerEmit.bind(this);
    this.updateLabel = updateLabel.bind(this);
  };

  async preload() {
    console.log(client.scenes.name.start);

    this.load.atlas('tiled_map_4_32', '../../assets/level/tileset/tiled_map_4_32.png', '../../assets/level/tileset/tiled_map_4_32.json');
    this.load.spritesheet('player_0', '../../assets/img/player/player_m_x32.png', {frameWidth:client.player.data.width, frameHeight:client.player.data.height});
    this.load.spritesheet('player_1', '../../assets/img/player/player_f_x32.png', {frameWidth:client.player.data.width, frameHeight:client.player.data.height});


    const levelKey = Object.keys(levels);
    levelKey.forEach(name => {
      this.load.tilemapTiledJSON(name, levels[name].path)
    });

    await fetch('/api/get-player')
    .then(response => response.json())
    .then(data => {
      const coord = this.convertCoordPlayerToMap(data.x, data.y);
      client.x = coord.x;
      client.y = coord.y;
      client.player.rotation = data.rotation;
      client.player.gender = data.gender;
      client.currentIndexScene = data.scene;
      this.updateLabel('quoicoucity');
    });
  };

  create() {
    client.map.tiles = this.textures.get('tiled_map_4_32').customData.tiles;

    this.createAnimationPlayer('player', 'idle_down', 1, 56, 56);
    this.createAnimationPlayer('player', 'idle_left', 1, 68, 68);
    this.createAnimationPlayer('player', 'idle_right', 1, 80, 80);
    this.createAnimationPlayer('player', 'idle_up', 1, 92, 92);

    this.createAnimationPlayer('player', 'down', 6, 57, 59);
    this.createAnimationPlayer('player', 'left', 6, 69, 71);
    this.createAnimationPlayer('player', 'right', 6, 81, 83);
    this.createAnimationPlayer('player', 'up', 6, 93, 95);

    this.createAnimationPlayer('player', 'run_down', 8, 104, 107);
    this.createAnimationPlayer('player', 'run_left', 8, 116, 119);
    this.createAnimationPlayer('player', 'run_right', 8, 128, 131);
    this.createAnimationPlayer('player', 'run_up', 8, 140, 143);


    setTimeout(() => {
      this.scene.start(client.scenes.name.world);
    }, client.settings.timeout.start);
  };
};

export default StartScene;