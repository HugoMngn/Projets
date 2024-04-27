import { client } from "../index.js";

function mapMove(teleport) {
  const level = client.map.currentLevel;
 
  const x = client.x * client.map.sizePixelTile;
  const y = client.y * client.map.sizePixelTile;
  if(!teleport) {
    this.tweens.add({
      targets: [level.bottomLayer, level.middle1Layer, level.collisionLayer, level.middle2Layer, level.topLayer1, level.topLayer2],
      x,
      y, 
      duration: this.updateInterval,
      ease: 'Linear'
    });
  } else {
    [level.bottomLayer.x, level.middle1Layer.x, level.collisionLayer.x, level.middle2Layer.x, level.topLayer1.x, level.topLayer2.x] = [x, x, x, x, x, x];
    [level.bottomLayer.y, level.middle1Layer.y, level.collisionLayer.y, level.middle2Layer.y, level.topLayer1.y, level.topLayer2.y] = [y, y, y, y, y, y];
  }
  
};

export { mapMove };