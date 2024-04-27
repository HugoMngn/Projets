import { client } from './utils/index.js';
import StartScene from './scenes/start.js';
import WorldScene from './scenes/world.js';
import StopScene from './scenes/stop.js';
import InventoryScene from './scenes/inventory.js';

new Phaser.Game({
  type: Phaser.AUTO,
  width: client.map.screenX,
  height: client.map.screenY,
  scene: [StartScene, WorldScene, StopScene, InventoryScene],
  //disableCrispText: true //anti ancrage mais marche pas
});