function createAnimationPlayer(label, key, frameRate, start, end, repeat=-1) {
  const labelM = label + '_0';
  const labelF = label + '_1';
  const keyM = labelM + '_' + key;
  const keyF = labelF + '_' + key;
  this.anims.create({
    key: keyM,
    frameRate,
    frames: this.anims.generateFrameNumbers(labelM, {start, end}),
    repeat
  });
  this.anims.create({
    key: keyF,
    frameRate,
    frames: this.anims.generateFrameNumbers(labelF, {start, end}),
    repeat
  });
};

export { createAnimationPlayer }
