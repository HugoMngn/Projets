import { client, convertCoordPlayerToMap } from '../index.js'

document.addEventListener('DOMContentLoaded', () => {
  const checkBoxCollision = document.getElementById('checkbox-collision');
  const rangeSliderScale = document.getElementById('rangeSlider-scale');
  const changeSkinButton = document.getElementById('player-change-skin');

  checkBoxCollision.addEventListener('change', () => {
    client.settings.collision = checkBoxCollision.checked;
  });

  rangeSliderScale.addEventListener('change', () => {
    client.player.player.setScale(rangeSliderScale.value);
    document.getElementById('rangeSlider-scale-label').innerHTML = `Scale: x${rangeSliderScale.value}`;
  });

  changeSkinButton.addEventListener('click', () => {
    client.player.gender = client.player.gender ? 0 : 1;
    this.multiplayerEmit('saveLastPosition')
  });


  //Calque map
  const checkBoxcalqueCollision = document.getElementById('checkbox-calque-collision');
  const checkBoxcalqueTop2 = document.getElementById('checkbox-calque-top2');
  const checkBoxcalqueTop1 = document.getElementById('checkbox-calque-top1');
  const checkBoxcalqueMiddle2 = document.getElementById('checkbox-calque-middle2');
  const checkBoxcalqueMiddle1 = document.getElementById('checkbox-calque-middle1');
  const checkBoxcalqueBottom = document.getElementById('checkbox-calque-bottom');

  checkBoxcalqueCollision.addEventListener('change', () => client.map.currentLevel.collisionLayer.setVisible(checkBoxcalqueCollision.checked));

  checkBoxcalqueTop2.addEventListener('change', () => client.map.currentLevel.topLayer2.setVisible(checkBoxcalqueTop2.checked));

  checkBoxcalqueTop1.addEventListener('change', () => client.map.currentLevel.topLayer1.setVisible(checkBoxcalqueTop1.checked));

  checkBoxcalqueMiddle2.addEventListener('change', () => client.map.currentLevel.middle2Layer.setVisible(checkBoxcalqueMiddle2.checked));

  checkBoxcalqueMiddle1.addEventListener('change', () => client.map.currentLevel.middle1Layer.setVisible(checkBoxcalqueMiddle1.checked));

  checkBoxcalqueBottom.addEventListener('change', () => client.map.currentLevel.bottomLayer.setVisible(checkBoxcalqueBottom.checked));
});

function updateLabel(currentMapName) {
  const coordPlayer = this.convertCoordPlayerToMap(client.x, client.y);
  document.getElementById('position-player').innerText = `player: x: ${coordPlayer.x}, y:${coordPlayer.y}`;
  document.getElementById('map-position').innerText = `map: x: ${client.x}, y:${client.y}`;
  document.getElementById('map-name').innerText = `[${client.currentIndexWorld}] ${currentMapName}`;


};

export { updateLabel };