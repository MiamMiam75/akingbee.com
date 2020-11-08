import { aristaeusApi, dealWithError, notificate } from '../../lib/common';

export async function getApiaries(callback) {
  await aristaeusApi.get(`/apiary`)
    .then((response) => {
      const data = response.data;
      callback({data});
    })
    .catch((error) => {
      if (!error.response) {
        notificate("error", error.message);
      } else {
        dealWithError(error);
      }
    });
}

export async function createApiary({name, location, status, honey_type}, callback) {
  await aristaeusApi.post(`/apiary`, {name, location, status, honey_type})
    .then((response) => {
      callback();
    })
    .catch((error) => {
      if (!error.response) {
        notificate("error", error.message);
      } else {
        dealWithError(error);
      }
    });
}