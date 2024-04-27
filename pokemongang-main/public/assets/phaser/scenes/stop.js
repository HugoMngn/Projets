import { client } from "../utils/index.js";

class StopScene extends Phaser.Scene {
  constructor() {
    super({key: client.scenes.name.stop});
    
  };

  async preload() {
    console.log(client.scenes.name.stop)
    setTimeout(() => {
      this.scene.start(client.scenes.name.world);
    }, client.settings.timeout.start);
  };

  create() {

  }
};

export default StopScene;