import './Virhe.css'

function Virhe({message}: {message: string}) {

  return (
      <div className='warning'>
        <p className='warningText'>
            {message}
        </p>
      </div>
  )
}

export default Virhe