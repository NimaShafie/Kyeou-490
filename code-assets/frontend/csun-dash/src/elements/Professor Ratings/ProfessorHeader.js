import { Button, Rating, Typography, Box, Modal  } from "@mui/material"
import {useState} from 'react'
import RatingsForm from "./RatingsForm"


function ProfessorHeader({professorSelected, subject}){
    const [rateModal, setRateModal] = useState(false)

    function handleRateModal(){
        setRateModal(!rateModal)
    }

    return(
        <div style={mainContainerStyle}>
            <div style={headerContainerStyle}>
                <h1 style={ratingStyle}>4.7/5</h1>
                <h3 style={totalRatingstyle}>Overall Quality Based on 7 ratings</h3>
                <h1 style={professorNameStyle}>Arin Gregorian</h1>
                <div style={professorStatsStyle}>
                    <div style={wouldTakeAgainStyle}>
                        <h2>100%</h2>
                        <h4>Would take again</h4>
                    </div>
                    <div style={difficultyStyle}>
                        <h2>3.1</h2>
                        <h4>Level of Difficulty</h4>
                    </div>
                </div>
                <Button style={rateButtonStyle} onClick={handleRateModal}>Rate Professor Gregorian</Button>
            </div>

            <div style={starsContainerStyle}>
                <div style={starsRatingsContainer}>
                    <Rating name="read-only" value={5} readOnly />
                    <Typography component="legend">5 ratings</Typography>
                </div>
                <div style={starsRatingsContainer}>
                    <Rating name="read-only" value={4} readOnly />
                    <Typography component="legend">2 ratings</Typography>
                </div>
                <div style={starsRatingsContainer}>
                    <Rating name="read-only" value={3} readOnly />
                    <Typography component="legend">0 ratings</Typography>
                </div>
                <div style={starsRatingsContainer}>
                    <Rating name="read-only" value={2} readOnly />
                    <Typography component="legend">0 ratings</Typography>
                </div>
                <div style={starsRatingsContainer}>
                    <Rating name="read-only" value={1} readOnly />
                    <Typography component="legend">0 ratings</Typography>
                </div>
            </div>

            <div>
                <Modal
                    open={rateModal}
                    onClose={handleRateModal}
                >
                    <Box sx={modalStyle}>
                        <Typography variant="h4" component="h2" style={{textAlign:"center"}}>
                            Post New Rating for <span style={{fontWeight:"bold"}}>{professorSelected}</span>
                        </Typography>
                        <RatingsForm 
                            rateModal={rateModal} 
                            setRateModal={setRateModal} 
                            professorSelected={professorSelected} 
                            subject={subject}>
                        </RatingsForm>
                    </Box>
                </Modal>
            </div>
            
        </div>
    )
}

export default ProfessorHeader

const mainContainerStyle = {
    display: "flex",
    justifyContent: "center",
    marginTop: "50px",
    
}

const headerContainerStyle = {
    backgroundColor: "#1C1C1C",
    color: "white",
    marginBottom: "50px"
}

const ratingStyle = {
    fontSize: "50px",
    fontWeight: "bold",
    paddingBottom: "8px"
}

const totalRatingstyle = {
    fontSize: "15px",
    paddingBottom: "8px"
}

const professorNameStyle = {
    fontSize: "50px",
    fontWeight: "bold",
    paddingBottom: "8px"
}

const professorStatsStyle = {
    display: "flex",
    paddingBottom: "8px"
}

const wouldTakeAgainStyle = {
    borderRight: "1px solid white",
    textAlign: "center",
    padding: "8px"
}

const difficultyStyle = {
    padding: "8px",
    textAlign: "center"
}

const rateButtonStyle = {
    backgroundColor: "blue",
    width: "250px",
    height: "35px",
    borderRadius: "15px",
    color: "white",
    fontWeight: "bold"
}

const starsContainerStyle = {
    marginLeft: "30px",
}

const starsRatingsContainer = {
    color: "white",
    display: "flex",
    padding: "10px"
}


const modalStyle = {
    position: 'absolute',
    top: '50%',
    left: '50%',
    transform: 'translate(-50%, -50%)',
    width: "75vw",
    height: "75vh",
    bgcolor: 'background.paper',
    border: '2px solid #000',
    boxShadow: 24,
    p: 4,
  };