import redis from 'redis';
import {promisify} from 'util';

const client = redis.createClient()

get = promisify(client.get).bind(client);

client.on('connect', () => console.log('Redis client connected to the server'));
client.on('error', err => console.log('Redis Client Error', err))

function setNewSchool(schoolName, value) {
    client.set(schoolName, value, redis.print);
}

async function displaySchoolValue(schoolName) {
    const reply =  await get(schoolName)
    console.log(reply);    
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');