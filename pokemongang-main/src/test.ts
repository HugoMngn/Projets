import { readdirSync } from 'fs';
import listItems from '../ressources/assets/json/items.json';
import jsonDataImage from '../public/assets/img/items/items_spritesheet.json';
import path from 'path';

const listeType:string[] = [
  'Pokeballs',    
  'Medicine',     
  'Battle items', 
  'General items',
  'Hold items',   
  'Key Items',    
  'Berries',      
  'Machines'      
]

const imageArray = readdirSync(path.join(__dirname, '../ressources/assets/sprites-master/sprites/items'));

type ItemMap = {
  id:number;
  name:string;
  type:number;
  description:string;
  image:string;
};

const itemMap = new Map<number, ItemMap>();

listItems.slice(500).forEach(i => { //
  const nameJson = i.name
  const name = (typeof nameJson != 'string' ? nameJson.english : 'place_holder')

  const image = (imageArray.find(x => x === name.replace(/ /gi, '-').replace(/é/gi, 'e').toLowerCase() + '.png') || 'data-card-01').replace('.png', '');

  const type = listeType.indexOf(i.type) + 1

  itemMap.set(
    i.id,
    {
      id: i.id,
      name: name.replace(/'/gi, "\\'"),
      type: type,
      description: i.description.replace(/'/gi, "\\'"),
      image: image
    }
  );
});

setTimeout(() => {
  itemMap.forEach(i => {
    const itemJson = jsonDataImage.find(x => x.name === i.image)!;
    const x = itemJson.position.x / 30;
    const y = (itemJson.position.y / 30) * 30;
    console.log(`UPDATE items SET spritesheet = ${x + y} WHERE id = ${i.id};`)
  })
}, 5000);


