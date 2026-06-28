import type { Metadata } from "next";
import "./globals.css";
import QueryProvider from "../providers/QueryProvider";
import AuthProvider from "../providers/AuthProvider";
import SessionGuard from "../components/auth/SessionGuard";

export const metadata: Metadata = {
  title: "AlphaForge AI Dashboard",
  description: "Production-grade quantitative research and paper trading platform",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body>
        <QueryProvider>
          <AuthProvider>
            <SessionGuard>{children}</SessionGuard>
          </AuthProvider>
        </QueryProvider>
      </body>
    </html>
  );
}