//map
const sizeChunck = 11;
const sizePixelTile = 32;

//rotation
const rotationUp = 0;
const rotationDown = 1;
const rotationRight = 2;
const rotationLeft = 3;

//player
const playerRotatation = rotationDown;//0:up,1:down,2:right,3:left,
const playerGender = 0;
//player data
const playerWidth = 25;
const playerHeight = 32;
const playerScale = 1.4;
const playerPoseCaseX = 6;  
const playerPoseCaseY = 6;  

//setting
const timeoutStart = 500;
const timeoutMenuSwitch = 50;
const speedPlayerWalk = 150;
const speedPlayerRun = 100; 

//animation
const playerIdleAnimations = ['idle_up', 'idle_down', 'idle_right', 'idle_left'];
const playerFirstAnimations = 1;
const playerLastAnimation = playerIdleAnimations[playerFirstAnimations];

//multiplayer
const multiplayerUsernameY = 20;

const socket = io();


const client = {
  x:0,
  y:0,
  currentIndexWorld: 0,
  map: {
    currentLevel: {},
    sizePixelTile,
    sizePixelChunck: sizeChunck * sizePixelTile,
    sizeChunck,
    screenX: sizeChunck * sizePixelTile,
    screenY: sizeChunck *  sizePixelTile,
    levels: [],
    tiles: {},
    tilesProperties:  {
      collision: 'collision',
      grass: 'grass',
      water: 'water'
    }
  },
  player: {
    freeze:false,
    rotation: playerRotatation,
    gender:playerGender,//0:M,1:F
    data: {
      width:playerWidth,
      height:playerHeight,
      scale: playerScale,
      poseCaseX: playerPoseCaseX,
      poseCaseY: playerPoseCaseY,
    },
    player: {}
  },
  settings: {
    collision:true,
    timeout: {
      start: timeoutStart,
      menuSwitch:timeoutMenuSwitch
    },
    speed: {
      walk: speedPlayerWalk,
      run: speedPlayerRun
    }
  },
  scenes: {
    name: {
      start: 'StartScene',
      world: 'WorldScene',
      stop: 'StopScene',
      inventory: 'InventoryScene'
    }
  },
  keys: {
    keys: {}
  },
  animation: {
    player: {
      rotation: {
        up: rotationUp,
        down: rotationDown,
        left: rotationLeft,
        right: rotationRight,
      },
      last: 'none',
      fisrt: playerLastAnimation,
      idles: playerIdleAnimations
    }
  },
  levelsData: {
    quoicoucity: {
      index: 0,
      name: 'quoicouity'
    }
  },
  multiplayer: {
    config: {
      usernameY: multiplayerUsernameY
    },
    socket,
    otherPlayers: {}
  }
}

export { client };