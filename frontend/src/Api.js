import axios from "axios";
import {base_url} from './Url'

class Api {
    static person_list() {
        return axios.get(base_url + '/person_list')
    }

    static article_list() {
        return axios.get(base_url + '/article_list')
    }

    static department_list() {
        return axios.get(base_url + '/department_list')
    }

    static get_article(id) {
        return axios.get(base_url + '/get_article', {
            params: {
                id: id,
            }
        })
    }

    static get_person(id) {
        return axios.get(base_url + '/get_person', {
            params: {
                id: id,
            }
        })
    }

    static get_department(id) {
        return axios.get(base_url + '/get_department', {
            params: {
                id: id,
            }
        })
    }
}

export default Api