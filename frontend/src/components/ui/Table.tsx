import React from "react";
import clsx from "clsx";

interface TableProps extends React.TableHTMLAttributes<HTMLTableElement> {}

export const Table: React.FC<TableProps> = ({ children, className, ...props }) => {
  return (
    <div className="w-full overflow-x-auto rounded border border-borderCustom">
      <table className={clsx("w-full border-collapse text-left text-sm", className)} {...props}>
        {children}
      </table>
    </div>
  );
};

export const TableHeader: React.FC<React.HTMLAttributes<HTMLTableSectionElement>> = ({ children, className, ...props }) => (
  <thead className={clsx("bg-secondaryBg border-b border-borderCustom text-xs font-semibold text-mutedCustom uppercase tracking-wider", className)} {...props}>
    {children}
  </thead>
);

export const TableBody: React.FC<React.HTMLAttributes<HTMLTableSectionElement>> = ({ children, className, ...props }) => (
  <tbody className={clsx("divide-y divide-borderCustom bg-cardBg", className)} {...props}>
    {children}
  </tbody>
);

export const TableRow: React.FC<React.HTMLAttributes<HTMLTableRowElement>> = ({ children, className, ...props }) => (
  <tr className={clsx("hover:bg-secondaryBg hover:bg-opacity-50 transition-colors", className)} {...props}>
    {children}
  </tr>
);

export const TableHead: React.FC<React.ThHTMLAttributes<HTMLTableCellElement>> = ({ children, className, ...props }) => (
  <th className={clsx("px-4 py-3 font-semibold", className)} {...props}>
    {children}
  </th>
);

export const TableCell: React.FC<React.TdHTMLAttributes<HTMLTableCellElement>> = ({ children, className, ...props }) => (
  <td className={clsx("px-4 py-3 text-white font-medium", className)} {...props}>
    {children}
  </td>
);
