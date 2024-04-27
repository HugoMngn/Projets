import { Router } from 'express';

import getItemsRoutes from './inventory/getItems';

const router = Router();

router.use('/get-items', getItemsRoutes);

export default router;