import React, {Component} from 'react'
import ReactDOM from 'react-dom'
import axios from "axios";
import ListDisplay from './ListDisplay'
import Api from "./Api";

class Main extends Component {
    state = {
        departments: [],
        persons: [],
        articles: [],
    }

    componentDidMount() {
        Api.person_list().then(res => {
            const persons = res.data.data
            this.setState({persons})
        })
        Api.article_list().then(res => {
            const articles = res.data.data
            this.setState({articles})
        })
        Api.department_list().then(res => {
            const departments = res.data.data
            this.setState({departments})
        })
    }

    render() {
        return (
            <div>
                <ListDisplay Title="文章列表" List={this.state.articles} Type="article"/>
                <ListDisplay Title="人员列表" List={this.state.persons} Type="person"/>
                <ListDisplay Title="部门列表" List={this.state.departments} Type="department"/>
            </div>
        )
    }
}

export default Main
