import React, {Component} from 'react'
import axios from "axios";
import ListDisplay from "./ListDisplay";
import Api from "./Api";
import TopBar from "./TopBar";

class Department extends Component {
    state = {
        data: {
            name: '',
            members: [],
            articles: [],
        }
    }

    componentDidMount() {
        Api.get_department(this.props.match.params.id).then(res => {
            const {data} = res.data
            console.log(data)
            this.setState({data})
        })
    }

    render() {
        return (
            <div>
                <TopBar/>
                <div>
                    <h1>{this.state.data.name}</h1>
                    <ListDisplay Title="成员" List={this.state.data.members} Type="person"/>
                    <ListDisplay Title="作品" List={this.state.data.articles} Type="article"/>
                </div>
            </div>
        )
    }
}

export default Department
