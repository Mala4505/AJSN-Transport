import React, { useState, useEffect } from "react";

import { Box } from "@mui/material";
import { DataGrid, GridToolbar } from "@mui/x-data-grid";
import { tokens } from "../../theme";
import Header from "../../components/Header";
import { useTheme } from "@mui/material";



const Drivers = () => {
  const theme = useTheme();
  const colors = tokens(theme.palette.mode);

  const [driver, setDriver] = useState([]);

  useEffect(() => {
    const setdriver = async () => {
      const res = await fetch("http://127.0.0.1:8000/administration/driver/");
      const getdata = await res.json();
      setDriver(getdata);
      // console.log(getdata);
    };
    setdriver();
  },[]);

  const columns = [
    { field: "Driver_ID", headerName: "ID", flex: 0.5 },
    {
      field: "Driver_Name",
      headerName: "Driver Name",
      flex: 1,
      cellClassName: "name-column--cell",
    },
    {
      field: "Mobile",
      headerName: "Mobile",
      headerAlign: "left",
      align: "left",
      flex: 1,
    },
    {
      field: "Email",
      headerName: "Email",
      flex: 1,
    },
    {
      field: "Address",
      headerName: "Address",
      flex: 1,
    },
    {
      field: "Active",
      headerName: "Active",
      flex: 1,
    },

  ];

  return (
    <Box m="20px" marginLeft="15vw" p="2rem" height="100%">
      <Header
        title="Drivers"
        subtitle="List of Drivers"
      />
      <Box
        m="40px 0 0 0"
        height="75vh"
        sx={{
          "& .MuiDataGrid-root": {
            border: "none",
          },
          "& .MuiDataGrid-cell": {
            borderBottom: "none",
          },
          "& .name-column--cell": {
            color: colors.greenAccent[300],
          },
          "& .MuiDataGrid-columnHeaders": {
            backgroundColor: colors.blueAccent[700],
            borderBottom: "none",
          },
          "& .MuiDataGrid-virtualScroller": {
            backgroundColor: colors.primary[400],
          },
          "& .MuiDataGrid-footerContainer": {
            borderTop: "none",
            backgroundColor: colors.blueAccent[700],
          },
          "& .MuiCheckbox-root": {
            color: `${colors.greenAccent[200]} !important`,
          },
          "& .MuiDataGrid-toolbarContainer .MuiButton-text": {
            color: `${colors.grey[100]} !important`,
          },
        }}
      >
        <DataGrid
          checkboxSelection
          rows={driver}
          columns={columns}
          getRowId={(row) => row.Driver_ID}
          components={{ Toolbar: GridToolbar }}
        />
      </Box>
    </Box>
  );
};

export default Drivers;