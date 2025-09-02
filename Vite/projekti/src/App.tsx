import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import Virhe from './virhe'

function App() {
  const [count, setCount] = useState(0)


  return (
    <>
      <Virhe message='AHTUNG AHTUNG WARNING APUA AAAAAAAH'/>
      <Virhe message='A'/>
    </>
  )
}



export default App
