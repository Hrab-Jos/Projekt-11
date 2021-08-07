import React from 'react'
import { render } from 'react-dom'
import Notifikace from './components/Main'

const container = document.getElementById('notifikace')
if (!!container) {
	render(<Notifikace />, container)
}