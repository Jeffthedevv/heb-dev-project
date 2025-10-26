import UploadForm from './components/UploadForm'
import DataTable from './components/DataTable'
import './App.css'

function App() {

  return (
    <div >
      <h1>H-E-B Data Tool</h1>
      <UploadForm />
      <hr style={{ margin: "16px 0" }} />
      <DataTable />
    </div>
  )
}

export default App
