import { client } from "../index.js";

function updateAnimationPlayer(name) {
  name = `player_${client.player.gender}_` + name
  if(client.animation.player.last != name) {
    client.animation.player.last = name;
    client.player.player.play(name);
    document.getElementById('anim-player').innerText = name;
  };
};

export { updateAnimationPlayer };