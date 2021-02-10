import React, {Component} from 'react'
import './index.css'

const NavigationBlock = (props) => {
    const rows = props.List.map((row, index) => {
        return (
            <li key={index}>{row.name}</li>
        )
    })
    return (
        <div>
            <h1>{props.Title}</h1>
            <ul>{rows}</ul>
        </div>
    )
}

export default NavigationBlock