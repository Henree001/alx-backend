import { express } from 'express';
import { createClient } from 'redis';
import { promisify } from 'util';

const listProducts = [[1, "Suitcase 250", 50, 4], [2, "Suitcase 450", 100, 10], [3, "Suitcase 650", 350, 2], [4, "Suitcase 1050", 550, 5]];

function getItemById(itemId) {
    const item = listProducts.find((product) => product[0] === itemId);
    return item;
    }
const app = express();
app.get('/list_products', (req, res) => {
    const arr = [];
    for (const item of listProducts) {
        arr.push({
            itemId: item[0],
            itemName: item[1],
            price: item[2],
            initialAvailableQuantity: item[3]
        }
        )
    }
    res.json(arr);
});

const client = createClient();
get = promisify(client.get).bind(client);

function reserveStockById(itemId){
    const item = getItemById(itemId);
    client.set(`item.${itemId}`, item[3]);
}

async function getCurrentReservedStockById(itemId){
    const reservedStock = await get(`item.${itemId}`);
    return reservedStock;
}

app.get('/lists_products/:itemId', async (req, res) => {
    const itemId = Number(req.params.itemId);
    const item = getItemById(itemId);
    if (!item) {
        res.status(404).json({ status: 'Product not found' });
        return;
    }
    const reservedStock = await getCurrentReservedStockById(itemId);
    res.json(
        {
            itemId: item[0],
            itemName: item[1],
            price: item[2],
            initialAvailableQuantity: item[3],
            currentQuantity: reservedStock
        }
    );
}
);

app.get('/reserve_product/:itemId', async (req, res) => {
    const itemId = Number(req.params.itemId);
    const item = getItemById(itemId);
    if (!item) {
        res.status(404).json({ status: 'Product not found' });
        return;
    }
    const reservedStock = await getCurrentReservedStockById(itemId);
    if (reservedStock <= 0) {
        res.status(403).json({ status: 'Not enough stock available', itemId });
        return;
    }
    reserveStockById(itemId);
    res.json({ status: 'Reservation confirmed', itemId });
}
);

app.listen(1245);

export default app;