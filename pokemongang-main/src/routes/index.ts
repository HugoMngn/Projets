import { Router } from 'express';
import userRoutes from './user';
import gameRoutes from './game';

//a modif
import getPlayerRoutes from './getPlayer';
import forceLeaveRoutes from './forceLeave';
import sessionErrorRoutes from './sessionErrorMessage';

const router = Router();

router.get('/', (req, res) => {
  res.send(200)
});

router.use('/user', userRoutes);
router.use('/game', gameRoutes)

//a modif
router.use('/get-player', getPlayerRoutes);
router.use('/force-leave', forceLeaveRoutes);
router.use('/get-session-error-message', sessionErrorRoutes);

export default router;