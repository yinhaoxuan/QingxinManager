import React, {Component} from 'react'

const ItemDisplay = (props) => {
    return (
        <a href={'#/' + props.Type + '/' + props.Data.id}>{props.Data.name}</a>
    )
}

export default ItemDisplay