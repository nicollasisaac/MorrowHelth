import { render } from 'solid-js/web'

import './styles/global.scss'
import Home from './home/Home'

const root = document.getElementById('root')

render(() => <Home />, root!)
