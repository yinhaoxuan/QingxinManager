import React, {Component} from 'react'
import './index.css'

const ItemDisplay = (props) => {
    return (
        <a href={'#/' + props.Type + '/' + props.Data.id}>{props.Data.name}</a>
    )
}

export default ItemDisplay