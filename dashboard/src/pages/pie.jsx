import React from "react";

import { Box } from "@mui/material";
import Header from "../components/Header";
import PieGraph from "../components/PieGraph";

const Pie = () => {
  return (
    <Box m="20px" p="2rem" height="100%">
      <Header title="Pie Chart" subtitle="Simple Pie Chart" />
      <Box height="75vh" width="75%" >
        <PieGraph />
      </Box>
    </Box>
  );
};

export default Pie;