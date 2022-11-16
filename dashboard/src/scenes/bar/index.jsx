import React from "react";

import { Box } from "@mui/material";
import Header from "../../components/Header";
import BarGraph from "../../components/BarGraph";

const Bar = () => {
  return (
    <Box m="20px">
      <Header title="Bar Chart" subtitle="Simple Bar Chart" />
      <Box height="75vh" width="75%" >
        <BarGraph />
      </Box>
    </Box>
  );
};

export default Bar;