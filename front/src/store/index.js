import Vue from 'vue'
import Vuex from 'vuex'
import api from "@/api";

Vue.use(Vuex)

export const TEST_ACTION = 'TEST_ACTION'
export const TEST_MUTATION = 'TEST_MUTATION'

export default new Vuex.Store({
  state: {
    isLoaderVisible: false,
  },
  getters: {
    isLoaderVisible: (state) => {
      return state.isLoaderVisible;
    },
  },
  mutations: {
    [TEST_MUTATION](state, value) {
      state.isLoaderVisible = value;
    },
  },
  actions: {
    async [TEST_ACTION]({ commit }) {
      const valueFromApi = (await api.get('')).data.success
      console.log({valueFromApi})
      commit(TEST_MUTATION, valueFromApi)
    },
  },
  modules: {
  },
  strict: true,
})

