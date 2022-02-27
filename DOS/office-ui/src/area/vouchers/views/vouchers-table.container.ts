import { connect } from "react-redux";
import { loadUsersAsCatalogAction } from "src/area/users/state/usecases/load-users-as-catalog.usecase";
import { loadStatusesAction } from "src/area/statuses/state/usecases/load-statuses.usecase";
import { userIsComunSelector } from "src/area/auth/state/auth.selectors";
import { ValesTable } from "./vouchers-table.component";
import { loadVouchersAction } from "../state/usecases/load-vouchers.usecase";
import { loadUnitsCatalogAction } from "src/area/units/state/usecases/load-units-catalog.usecase";
// import { deleteVoucherAction } from "../state/usecases/delete-voucher.usecase";
// import { permissionSelector } from 'src/area/auth/state/auth.selectors';
import {
  isLoadingSelector,
  vouchersCatalogSelector,
  pagingSelector,
  filtersSelector,
} from "../state/vouchers.selectors";

const mapDispatchToProps = {
  // deleteVoucherAction,
  loadVouchersAction,
  loadUsersAsCatalogAction,
  loadStatusesAction,
  loadUnitsCatalogAction,
};

function mapStateToProps(state: any) {
  return {
    vouchers: vouchersCatalogSelector(state),
    loading: isLoadingSelector(state),
    paging: pagingSelector(state),
    // isAllowed: permissionSelector(state),
    filters: filtersSelector(state),
    userIsComun: userIsComunSelector(state),
  };
}

export const VouchersTableContainer = connect(
  mapStateToProps,
  mapDispatchToProps
)(ValesTable);
