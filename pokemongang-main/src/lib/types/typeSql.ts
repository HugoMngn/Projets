import { MysqlError } from "mysql";
import { PlayerGender } from "./enum";

type MysqlItems = {
  id:number;
  name:string;
  type:number;
  description:string;
  spritesheet:string;
};

type MysqlItemsUsers = {
  id:number;
  id_user:number;
  id_item:number;
  value:number;
};

type MysqlItemType = {
  id:number;
  name:string;
};

type MysqlUser = {
  id:number;
  token:string;
  username:string;
  password:string;
  x:number;
  y:number;
  rotation:number;
  world:number;
  gender:PlayerGender;
};

export type ListeTables = 'items' | 'items_users' | 'item_type' |'users'

export type MysqlPokemonGang<T extends ListeTables> = 
T extends 'items' ? MysqlItems[] :
T extends 'items_users' ? MysqlItemsUsers[] :
T extends 'item_type' ? MysqlItemType[] :
T extends 'users' ? MysqlUser[] :
undefined | MysqlError;