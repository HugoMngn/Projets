import { client, createKeyboard, createLayer } from "../utils/index.js";

const frimeSizeHud = 352;
const frimeSizeItem = 30;
const sizeItems = 37;
const totalItemsInHud = 5;



function wrapText(text, pixelsPerCharacter=5, maxWidth=314) {
    const charactersPerLine = Math.floor(maxWidth / pixelsPerCharacter);

    const words = text.split(' ');
    let currentLine = '';
    let wrappedText = '';

    for (let i = 0; i < words.length; i++) {
        let testLine = currentLine + words[i] + ' ';

        if (testLine.length > charactersPerLine && i > 0) {
            wrappedText += currentLine + '\n';
            currentLine = words[i] + ' ';
        } else {
            currentLine = testLine;
        }
    }

    wrappedText += currentLine;
    return wrappedText.trim();
}


class InventoryScene extends Phaser.Scene {
  constructor() {
    super({key: client.scenes.name.inventory});
    this.layer = {};
    this.lastUpdateTime = 0;
    this.updateInterval = 100;
    this.itemsJson = {};

    this.selectItem = {};
    
    //l'item en bas description
    this.spriteItemSelect = {};
    this.spriteItemName = {};
    this.spriteItemDescription = {};

    this.textNavBar = {};

    this.createKeyboard = createKeyboard.bind(this);
    this.createLayer = createLayer.bind(this);  
    
    this.navBarLabels = ['Poche Soins', 'Poche Poké Balls', 'Poche Objets de combat', 'Poche Baies', 'Poche Objets', 'Poche CT', 'Poche Trésors', 'Poche Objets rares'];
    
    this.itemPosition = {
      x: 20,
      y: 105,
      index: 0,
      indexSelect: 0,
      navBarIndex: 0
    }
  };

  async preload() {
    console.log(this.scene.key);
    this.load.spritesheet('items_spritesheet', '../../assets/img/items/items_spritesheet.png', {frameWidth:frimeSizeItem, frameHeight:frimeSizeItem});
    this.load.spritesheet('hud_items_menu', '../../assets/img/items/hud_items_menu.png', {frameWidth:frimeSizeHud, frameHeight:frimeSizeHud});
    this.load.spritesheet('hud_nav_bar_blip', '../../assets/img/items/hud_nav_bar_blip.png', {frameWidth:20, frameHeight:20});


    this.createKeyboard();
    this.createLayer();
  };
  
  async create() {
    const response = await fetch('/api/game/get-items');
    this.itemsJson = await response.json();

    const backgroundHud = this.add.sprite(0, 0, 'hud_items_menu', 0).setOrigin(0, 0);
    const topHud = this.add.sprite(0, 0, 'hud_items_menu', 1).setOrigin(0, 0);
    

    this.layer.background.add(backgroundHud);
    this.layer.top.add(topHud);
    

    if(this.itemsJson.items.length) { 
      this.selectItem = this.add.sprite(0, 0, 'hud_items_menu', 2).setOrigin(0, 0);
      this.layer.top.add(this.selectItem);

      this.spriteItemSelect = this.add.sprite(this.itemPosition.x, 288, 'items_spritesheet', this.itemsJson.items[0].spritesheet).setOrigin(0, 0).setScale(0.66);
      this.spriteItemName = this.add.text(this.itemPosition.x + 40, 290, this.itemsJson.items[0].name, {
        fontFamily: 'W95FA',
        color: '#000000',
        fontSize: 13
      }).setOrigin(0, 0);
      
      const wrappedText = wrapText(this.itemsJson.items[0].description)

      this.spriteItemDescription = this.add.text(this.itemPosition.x, 312, wrappedText, {
        fontFamily: 'W95FA',
        color: '#000000',
        fontSize: 13
      }).setOrigin(0, 0);
    };

    this.itemsJson.items.forEach(i => {
      const item = this.add.sprite(this.itemPosition.x, this.itemPosition.y, 'items_spritesheet', i.spritesheet).setOrigin(0, 0);
      const nameItem = this.add.text(this.itemPosition.x + 40, this.itemPosition.y + 7, i.name, {
        fontFamily: 'W95FA',
        color: '#000000'
      }).setOrigin(0);

      const valueX = this.add.text(this.itemPosition.x + 260, this.itemPosition.y + 7, 'x', {
        fontFamily: 'W95FA',
        color: '#000000'
      }).setOrigin(0)

      const value = this.add.text(this.itemPosition.x + 310, this.itemPosition.y + 7, i.value.toString(), {
        fontFamily: 'W95FA',
        color: '#000000'
      }).setOrigin(1, 0)

      this.layer.items.add([item, nameItem, valueX, value])
      this.itemPosition.y += sizeItems;
    });

    this.textNavBar = this.add.text(this.game.config.width / 2 + 40, 70, this.navBarLabels[this.itemPosition.navBarIndex], {
      fontFamily: 'W95FA',
      color: '#ffffff'
    }).setOrigin(0.5, 0);
    this.layer.top.add(this.textNavBar);

    let xNavBarBlip = 120
    this.navBarLabels.forEach((value, index) => {
      const frame = index === this.itemPosition.navBarIndex ? index + this.navBarLabels.length : index;
      const spriteBlipNavBar = this.add.sprite(xNavBarBlip, 50, 'hud_nav_bar_blip', frame).setOrigin(0, 0);
      this.layer.navBarBlip.add(spriteBlipNavBar)
      xNavBarBlip += 25
    });


    this.itemPosition.y = 105;
  };

  update(time, delta) {
    if (time - this.lastUpdateTime >= this.updateInterval) {
      const keys = client.keys.keys;
      const upKey = keys.up.isDown;
      const downKey = keys.down.isDown;
      const rightKey = keys.right.isDown;
      const leftKey = keys.left.isDown;

      if(upKey || downKey) {
        const totalItems =  this.itemsJson.items.length;
        if(this.itemsJson.items.length) {
          if(downKey) {
            this.itemPosition.index = Math.max(this.itemPosition.index - 1, totalItemsInHud - totalItems);
            this.itemPosition.indexSelect = Math.max(this.itemPosition.indexSelect - 1, 0 - totalItems);
            if(this.itemPosition.indexSelect < -2 && this.itemPosition.indexSelect > -7) {
              this.tweens.add({
                targets: this.selectItem,
                y: (this.itemPosition.indexSelect + 2) * -sizeItems,
                duration: this.updateInterval,
                ease: 'Linear'
              });
            };
  
          } else if(upKey) {
            if(this.itemPosition.indexSelect >= -2) this.itemPosition.index = Math.min(this.itemPosition.index + 1, 0);
            this.itemPosition.indexSelect = Math.min(this.itemPosition.indexSelect + 1, 0);
            if(this.itemPosition.indexSelect <= -2) {
              this.tweens.add({
                targets: this.selectItem,
                y: (this.itemPosition.indexSelect + 2) * -sizeItems,
                duration: this.updateInterval,
                ease: 'Linear'
              });
            };
          };
        };

       

        const selectedItem = this.itemsJson.items[this.itemPosition.indexSelect * -1]
        if(selectedItem) {
          this.spriteItemSelect.setFrame(selectedItem.spritesheet);
          this.spriteItemName.setText(selectedItem.name);
          const wrappedText = wrapText(selectedItem.description)
          this.spriteItemDescription.setText(wrappedText)
        };
        //console.log(this.itemPosition.index, this.itemPosition.indexSelect)

        this.tweens.add({
          targets: this.layer.items,
          y: this.itemPosition.index * sizeItems,
          duration: this.updateInterval,
          ease: 'Linear'
        });

        this.lastUpdateTime = time;
      } else if(rightKey || leftKey) {
        let moving = 0;
        if(rightKey) {
          this.itemPosition.navBarIndex = Math.min(this.itemPosition.navBarIndex + 1, this.navBarLabels.length - 1);
          moving = -1; 
        } else if(leftKey) {
          this.itemPosition.navBarIndex = Math.max(this.itemPosition.navBarIndex - 1, 0);
          moving = 1;
        };

        const ongletSelected = this.layer.navBarBlip.list[this.itemPosition.navBarIndex];
        const beforeOngletSelected = this.layer.navBarBlip.list[this.itemPosition.navBarIndex + moving];
        if(ongletSelected) {
          ongletSelected.setFrame(this.itemPosition.navBarIndex + this.navBarLabels.length);
        };
        if(beforeOngletSelected) {
          beforeOngletSelected.setFrame(this.itemPosition.navBarIndex + moving);
        }

        this.lastUpdateTime = time;
      } else {

      }
    };
  };
};

export default InventoryScene;