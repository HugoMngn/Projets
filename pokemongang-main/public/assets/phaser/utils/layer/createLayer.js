import { client } from "../index.js";

function createLayer() {
  if(this.scene.key === client.scenes.name.world) {
    this.layer = {
      background: this.add.layer(),
      player: this.add.container(0, 0),
      top: this.add.layer(),
      text: this.add.container(0, 0)
    } 
  } else if(this.scene.key === client.scenes.name.inventory) {
    this.layer = {
      background: this.add.container(0, 0),
      items: this.add.container(0, this.itemPosition.index * 37),
      top: this.add.container(0, 0),
      navBarBlip: this.add.container(0, 0),
    }
  }
};

export { createLayer };