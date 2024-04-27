import { client, createMap, createPlayer, createLayer, createKeyboard, playerMove, mapMove, updateAnimationPlayer, convertCoordMapToPlayer, convertCoordPlayerToMap, updateLabel, updateOtherPlayer, multiplayerWorld, multiplayerEmit, createOtherPlayer } from '../utils/index.js';

class WorldScene extends Phaser.Scene {
  constructor() {
    super({key: client.scenes.name.world});
    this.layer = {};

    this.lastUpdateTime = 0;
    this.updateInterval = client.settings.speed.walk;
    
    this.createLayer = createLayer.bind(this);
    this.createMap = createMap.bind(this);
    this.createPlayer = createPlayer.bind(this);
    this.createKeyboard = createKeyboard.bind(this);
    this.playerMove = playerMove.bind(this);
    this.mapMove = mapMove.bind(this);
    this.updateAnimationPlayer = updateAnimationPlayer.bind(this);
    this.convertCoordMapToPlayer = convertCoordMapToPlayer.bind(this);
    this.convertCoordPlayerToMap = convertCoordPlayerToMap.bind(this);
    this.updateLabel = updateLabel.bind(this);
    this.updateOtherPlayer = updateOtherPlayer.bind(this);

    this.multiplayerWorld = multiplayerWorld.bind(this);
    this.multiplayerEmit = multiplayerEmit.bind(this);
    this.createOtherPlayer = createOtherPlayer.bind(this);
  };

  async preload() {
    console.log(this.scene.key);

    this.createKeyboard();
  };

  create() {
    this.createLayer();
    this.createMap();
    this.createPlayer();
    this.multiplayerWorld();

    
    
  };

  update(time, delta) {
    if(!client.player.freeze)  this.playerMove(time);
  }
};

export default WorldScene;