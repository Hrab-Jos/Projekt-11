import React from 'react'
import { render } from 'react-dom'
import Notifikace from './components/Main'

const container = document.getElementById('notifikace')
if (!!container) {
	console.log(container)
	let data = container.dataset.list
	const userid = container.dataset.userid
	if (!!data) {
		data = JSON.parse(data)
	}
	render(<Notifikace notifications={data} userid={userid} />, container)
}