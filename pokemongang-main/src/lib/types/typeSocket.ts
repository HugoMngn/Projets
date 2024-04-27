import { PlayerGender, PlayerRotation } from "../index";

//playerMove
type SocketPlayerMove = { 
  x:number;
  y:number;
  rotation:number;
  teleport:boolean;
  animation:string;
  socketId:string;
  gender:PlayerGender;
  scene:number;
  world:number;
};

//saveLastPosition
type SocketSaveLastPos = {
  x:number;
  y:number;
  rotation:PlayerRotation;
  world:number;
  gender:PlayerGender;
}

//loginAttempt
type SocketLoginAttempt = {
  username:string;
  password:string;
};

export type ListeSocket = 'playerMove' | 'saveLastPosition' | 'loginAttempt'

export type SocketPokemon<T extends ListeSocket> = 
T extends 'playerMove' ? SocketPlayerMove :
T extends 'saveLastPosition' ? SocketSaveLastPos :
T extends 'loginAttempt' ? SocketLoginAttempt :
undefined;