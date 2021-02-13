import React, {Component} from 'react'
import './index.css'

const ListDisplay = (props) => {
    const rows = props.List.map((row, index) => {
        return (
            <li key={index}><a href={'#/' + props.Type + '/' + row.id}>{row.name}</a></li>
        )
    })
    return (
        <div>
            <h1>{props.Title}</h1>
            <ul>{rows}</ul>
        </div>
    )
}

export default ListDisplay