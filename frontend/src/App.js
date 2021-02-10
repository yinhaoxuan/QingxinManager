import React, {Component} from 'react'
import ReactDOM from 'react-dom'
import './index.css'
import axios from "axios";
import NavigationBlock from './NavigationBlock'

class App extends Component {
    state = {
        departments: [],
        persons: [],
        articles: [],
    }

    componentDidMount() {
        axios.get('http://127.0.0.1:8000/api/person_list')
            .then(res => {
                const persons = res.data.data
                this.setState({persons})
            })
        axios.get('http://127.0.0.1:8000/api/article_list')
            .then(res => {
                const articles = res.data.data
                this.setState({articles})
            })
        axios.get('http://127.0.0.1:8000/api/department_list')
            .then(res => {
                const departments = res.data.data
                this.setState({departments})
            })
    }

    render() {
        return (
            <div>
                <NavigationBlock Title="文章列表" List={this.state.articles} Type="article"/>
                <NavigationBlock Title="人员列表" List={this.state.persons} Type="person"/>
                <NavigationBlock Title="部门列表" List={this.state.departments} Type = "department"/>
            </div>
        )
    }
}

export default App