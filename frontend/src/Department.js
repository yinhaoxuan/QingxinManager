import React, {Component} from 'react'
import axios from "axios";
import ListDisplay from "./ListDisplay";

class Department extends Component {
    state = {
        data: {
            name: '',
            members: [],
            articles: [],
        }
    }

    componentDidMount() {
        axios.get('http://127.0.0.1:8000/api/get_department', {
            params: {
                id: this.props.match.params.id
            }
        })
            .then(res => {
                const {data} = res.data
                console.log(data)
                this.setState({data})
            })
    }

    render() {
        return (
            <div>
                <h1>{this.state.data.name}</h1>
                <ListDisplay Title="成员" List={this.state.data.members} Type="person"/>
                <ListDisplay Title="作品" List={this.state.data.articles} Type="article"/>
            </div>
        )
    }
}

export default Department