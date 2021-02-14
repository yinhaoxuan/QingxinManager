import React, {Component} from 'react'
import axios from "axios";
import ListDisplay from "./ListDisplay";
import ItemDisplay from "./ItemDisplay";

class Person extends Component {
    state = {
        data: {
            name: '',
            id_number: '',
            department: '',
            wrote: [],
            edited: [],
        }
    }

    componentDidMount() {
        axios.get('/api/get_person', {
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
                <p>{"学号：" + this.state.data.id_number}</p>
                <p>部门：<ItemDisplay Data={this.state.data.department} Type="department" /></p>
                <ListDisplay Title="写作作品" List={this.state.data.wrote} Type="article"/>
                <ListDisplay Title="责编作品" List={this.state.data.edited} Type="article"/>
            </div>
        )
    }
}

export default Person
