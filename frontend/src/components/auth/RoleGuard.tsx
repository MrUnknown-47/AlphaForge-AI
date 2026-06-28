"use client";

import React from "react";
import { useAuthStore } from "../../store/authStore";

interface RoleGuardProps {
  allowedRoles: string[];
  children: React.ReactNode;
  fallback?: React.ReactNode;
}

export const RoleGuard: React.FC<RoleGuardProps> = ({
  allowedRoles,
  children,
  fallback = <div className="p-4 text-xs font-semibold text-dangerCustom uppercase tracking-wider bg-cardBg border border-borderCustom rounded">Access Denied: Insufficient Permissions</div>
}) => {
  const { role } = useAuthStore();

  if (!role || !allowedRoles.includes(role.toUpperCase())) {
    return <>{fallback}</>;
  }

  return <>{children}</>;
};
export default RoleGuard;
