import { Router } from "express";
import loginRoutes from './login';

const router = Router();
router.get('/', (req, res) => {
  res.send(200)
});

router.use('/login', loginRoutes);

export default router;