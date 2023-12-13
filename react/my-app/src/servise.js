import axios from 'axios'

const getAll = (url) => axios.get(url);

const getById = (url,userId) => axios.get(`${url}/${userId}`);

const addItem = (url, obj) => axios.post(url, obj);

const updateItem = (url, userId, obj) => axios.patch(`${url}/${userId}`, obj);


export  { addItem, getById, getAll, updateItem};