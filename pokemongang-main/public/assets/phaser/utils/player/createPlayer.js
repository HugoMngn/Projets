import { client } from "../index.js";

function createPlayer() {
  const player = this.add.sprite(this.game.config.width / 2, this.game.config.height / 2, `player_0`)
  .setScale(client.player.data.scale)

  this.textures.get('player_0').setFilter(Phaser.Textures.FilterMode.NEAREST);
  this.textures.get('player_1').setFilter(Phaser.Textures.FilterMode.NEAREST);

  client.player.player = player;
  player.setScale(client.player.data.scale);

  const animationName = `player_${client.player.gender}_` + client.animation.player.fisrt;
  client.animation.player.last = animationName;
  
  player.play(animationName);
  this.layer.player.add(player);
};

export { createPlayer };