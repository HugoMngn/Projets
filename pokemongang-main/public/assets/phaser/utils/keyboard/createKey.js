import { client, levels } from '../index.js';

function createKeyboard() {
  this.input.keyboard.removeAllKeys();

  if(this.scene.key === client.scenes.name.world) {
    client.keys.keys = this.input.keyboard.addKeys({
      up: Phaser.Input.Keyboard.KeyCodes.Z,
      down: Phaser.Input.Keyboard.KeyCodes.S,
      left: Phaser.Input.Keyboard.KeyCodes.Q,
      right: Phaser.Input.Keyboard.KeyCodes.D,
      shift: Phaser.Input.Keyboard.KeyCodes.SHIFT,
      e: Phaser.Input.Keyboard.KeyCodes.E,

      p: Phaser.Input.Keyboard.KeyCodes.P,
      m: Phaser.Input.Keyboard.KeyCodes.M,

      i: Phaser.Input.Keyboard.KeyCodes.I
    });

    this.input.keyboard.on('keydown-SHIFT', event => {
      this.updateInterval = client.settings.speed.run;
    });
    this.input.keyboard.on('keyup-SHIFT', event => {
      this.updateInterval = client.settings.speed.walk;
    });

    this.input.keyboard.on('keydown-I', event => {
      this.scene.start(client.scenes.name.stop)
    })

    this.input.keyboard.on('keydown-P', event => {
      this.scene.restart();
      const keysLevel = Object.keys(levels);
      client.currentIndexWorld = Math.min(client.currentIndexWorld + 1, keysLevel.length - 1);
    })

    this.input.keyboard.on('keydown-M', event => {
      this.scene.restart();
      client.currentIndexWorld = Math.max(client.currentIndexWorld - 1, 0);
    });

    setTimeout(() => {
      this.input.keyboard.on('keydown-E', event => { //world → inventory
        this.scene.start(client.scenes.name.inventory)
      });
    }, client.settings.timeout.menuSwitch);
  } else if(this.scene.key === client.scenes.name.inventory) {
    client.keys.keys = this.input.keyboard.addKeys({
      up: Phaser.Input.Keyboard.KeyCodes.Z,
      down: Phaser.Input.Keyboard.KeyCodes.S,
      left: Phaser.Input.Keyboard.KeyCodes.Q,
      right: Phaser.Input.Keyboard.KeyCodes.D,
      
      esc: Phaser.Input.Keyboard.KeyCodes.ESC,
      i: Phaser.Input.Keyboard.KeyCodes.I
    });

    setTimeout(() => {
      this.input.keyboard.on('keydown-E', event => { //inventory → world
        this.scene.start(client.scenes.name.world)
      });
    }, client.settings.timeout.menuSwitch);
  };
};

export { createKeyboard };