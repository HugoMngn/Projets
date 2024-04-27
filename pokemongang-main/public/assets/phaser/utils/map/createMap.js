import { client } from '../client/createClient.js';
//import './level/createLevel.js';

const levels = {

};

class CreateLevel {
  constructor(
    name,
    index,
    chunckSizeX,
    chunckSizeY,
    door,
  ) {
    this.path = '../../assets/level/world/' + name + '.json';

    levels[name] = {
      name,
      totalCaseX: chunckSizeX * client.map.sizeChunck,
      totalCaseY: chunckSizeY * client.map.sizeChunck,
      index,
      path: this.path,
      chunckSizeX,
      chunckSizeY,
      leftX: 0 - client.map.screenX / 2,
      rightX: client.map.sizePixelChunck * chunckSizeX + client.map.screenX / 2,
      topX: 0 - client.map.screenY / 2,
      bottomX: client.map.sizePixelChunck * chunckSizeY + client.map.screenY / 2,
      door,
    };
  };
};

new CreateLevel('quoicoucity', 0, 4, 9,
  [
    { case: [[0, -8, -21]], target: [0, 2, -65] },
    { case: [[1, 2, -66], [1, 1, -66], [1, 3, -66]], target: [1, -8, -22] }
  ],
);
new CreateLevel('feurcity', 1, 7, 7, [],);

new CreateLevel('gtaVIbeachbaby', 2, 9, 8,
  [
    { case: [[0, -47, -11]], target: [0, 0, -66] },   /*centre poke entrée*/
    { case: [[1, 0, -67]], target: [1, -47, -12] },   /*centre poke sortie*/

    { case: [[0, -47, -16]], target: [0, -18, -70] },   /* poke store entrée*/
    { case: [[1, -18, -70]], target: [1, -47, -17] },   /*poke store sortie*/

    { case: [[0, -56, -19]], target: [0, 1, -81] },   /*mini maison 1 entrée*/
    { case: [[1, 1, -82]], target: [1, -56, -19] },   /*mini maison 1 sortie*/

    { case: [[0, -60, -19]], target: [0, -20, -81] }, /* mini maison 2 entrée*/
    { case: [[1, -20, -82]], target: [1, -60, -19] }, /*mini maison 2 sortie*/

    { case: [[0, -6, -5]], target: [0, -17, -58] },   /*grotte bas entrée*/
    { case: [[3, -6, -5]], target: [3, -17, -58] },   /*grotte coté entrée*/
    { case: [[0, -6, -5]], target: [0, -17, -58] },   /*grotte bas sortie*/
    { case: [[3, -6, -5]], target: [3, -17, -58] },   /*grotte coté sortie*/

    { case: [[0, -58, -9]], target: [0, -62, -64] },    /*grande maison entrée*/
    { case: [[1, -62, -65]], target: [1, -58, -10] }     /*grande maison sortie */
  ]
);

function createMap() {
  const levelKey = Object.keys(levels);
  const sizePixelTile = client.map.sizePixelTile;
  const playerX = client.x;
  const playerY = client.y;

  client.map.currentLevel = {};
  client.map.levels = [];

  levelKey.forEach(name => {
    const level = levels[name];
    if (level.index === client.currentIndexWorld) client.map.levels.push(level);
  });
  const level = client.map.levels.find(i => i.index === client.currentIndexWorld);
  if (level) {
    const x = client.map.sizePixelTile * playerX;
    const y = client.map.sizePixelTile * playerY;

    const map = this.make.tilemap({ key: level.name });
    const tileset = map.addTilesetImage('tiled_map_4_32', 'tiled_map_4_32');

    const bottomLayer = map.createLayer('bottom', tileset, x, y);
    const middle1Layer = map.createLayer('middle1', tileset, x, y);
    const middle2Layer = map.createLayer('middle2', tileset, x, y);
    const topLayer1 = map.createLayer('top1', tileset, x, y);
    const topLayer2 = map.createLayer('top2', tileset, x, y);
    const collisionLayer = map.createLayer('collision', tileset, x, y);

    collisionLayer.setVisible(false);

    this.layer.background.add(bottomLayer);
    this.layer.background.add(middle1Layer);
    this.layer.background.add(middle2Layer);
    this.layer.top.add(topLayer1);
    this.layer.top.add(topLayer2);
    this.layer.top.add(collisionLayer);

    client.map.currentLevel = {
      level,
      map,
      tileset,
      bottomLayer,
      middle1Layer,
      middle2Layer,
      topLayer1,
      topLayer2,
      collisionLayer,
    };
  };
};



export { levels, CreateLevel, createMap };