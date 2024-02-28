import redis from 'redis';

const client = redis.createClient()

client.on('connect', () => console.log('Redis client connected to the server'));
client.on('error', err => console.log('Redis Client Error', err))

function setNewSchool(schoolName, value) {
    client.set(schoolName, value, redis.print);
}

function displaySchoolValue(schoolName) {
    client.get(schoolName, (error, reply) => {
        console.log(reply);
    });
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');