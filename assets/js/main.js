/* eslint-disable no-unused-vars */
function openPortfolioModal(url) {
  /* eslint-diable no-undef */
  const portfolioModal = new bootstrap.Modal("#modal-portfolio", {
    keyboard: false,
  });
  const portfolioPreview = document.getElementById("portfolio-preview");
  portfolioPreview.setAttribute("src", url);
  portfolioModal.show();
}
