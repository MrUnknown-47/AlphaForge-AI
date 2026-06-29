import React from "react";
import clsx from "clsx";

interface DataGridProps {
  items: Record<string, any>[];
  columns: { key: string; header: string; render?: (val: any) => React.ReactNode }[];
  className?: string;
}

export const DataGrid: React.FC<DataGridProps> = ({ items, columns, className }) => {
  return (
    <div className={clsx("w-full overflow-x-auto rounded border border-borderCustom bg-cardBg", className)}>
      <table className="w-full text-left text-sm border-collapse">
        <thead className="bg-secondaryBg border-b border-borderCustom text-xs text-mutedCustom uppercase tracking-wider">
          <tr>
            {columns.map((col) => (
              <th key={col.key} className="px-4 py-3 font-semibold">
                {col.header}
              </th>
            ))}
          </tr>
        </thead>
        <tbody className="divide-y divide-borderCustom">
          {items.length === 0 ? (
            <tr>
              <td colSpan={columns.length} className="px-4 py-6 text-center text-mutedCustom font-medium">
                No records found.
              </td>
            </tr>
          ) : (
            items.map((item, idx) => (
              <tr key={idx} className="hover:bg-secondaryBg hover:bg-opacity-50 transition-colors">
                {columns.map((col) => (
                  <td key={col.key} className="px-4 py-3 text-white">
                    {col.render ? col.render(item[col.key]) : item[col.key]}
                  </td>
                ))}
              </tr>
            ))
          )}
        </tbody>
      </table>
    </div>
  );
};
