import React, { useEffect, useState } from "react";
import api from "../services/api";

interface KPI {
  id: number;
  date: string;
  revenue: number;
  users: number;
}

export default function KPIs() {
  const [kpis, setKpis] = useState<KPI[]>([]);
  useEffect(() => {
    api.get("/kpis").then((res) => {
      setKpis(res.data);
    });
  }, []);

  return (
    <div>
      <h1 className="text-2xl font-bold mb-4">KPI Dashboard</h1>
      <ul>
        {kpis.map((kpi) => (
          <li key={kpi.id}>
            <strong>{kpi.date}</strong>: Revenue = {kpi.revenue}, Users = {kpi.users}
          </li>
        ))}
      </ul>
    </div>
  );
}